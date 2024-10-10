SELECT u.id, u.email, COUNT(l.id) AS link_count, u.date_joined
FROM api_user u
LEFT JOIN api_link l ON u.id = l.user_id
GROUP BY u.id
ORDER BY link_count DESC, u.date_joined ASC
LIMIT 10;