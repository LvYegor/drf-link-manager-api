from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Link, Collection
from .serializers import LinkSerializer, CollectionSerializer
from .scraper import scrape_og_data
from requests.exceptions import RequestException
from rest_framework import serializers


class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        url = self.request.data.get('url')

        if not url:
            raise serializers.ValidationError({'url': 'URL is required'})

        try:
            title, description, image, link_type = scrape_og_data(url)

            serializer.save(
                title=title,
                description=description,
                url=url,
                image=image,
                link_type=link_type,
                user=self.request.user
            )
        except RequestException:
            raise serializers.ValidationError({'url': 'Invalid URL or request failed'})
        except Exception as e:
            raise serializers.ValidationError({'error': str(e)})

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CollectionViewSet(viewsets.ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        collection = serializer.save(user=self.request.user)
        links = self.request.data.get('links', [])
        for link_id in links:
            try:
                link = Link.objects.get(id=link_id, user=self.request.user)
                collection.links.add(link)
            except Link.DoesNotExist:
                raise serializers.ValidationError(
                    {'links': f'Link with id {link_id} does not exist or does not belong to the user.'})
