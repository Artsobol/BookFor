## 1. Аутентификация и пользователи

### POST  
Регистрация: `/api/auth/register`
Авторизация: `/api/auth/login`
Выход: `/api/auth/logout`

### GET  
Получить всех пользователей: `/api/users`

Получить пользователя по `id`: `/api/users/{userId}`

### PUT  
Изменить пользователя по id: `/api/users/{userId}`

### DELETE  
Удалить пользователя по id: `/api/users/{userId}`

---

## 2. Книги

### GET  
Получить все книги: `/api/books`

Получить книгу по `id`: `/api/books/{bookId}`  

Получить книгу по `slug`: `/api/books/{bookSlug}`

### POST  
Добавить книгу: `/api/books`

### PUT  
Изменить книгу по `id`: `/api/books/{bookId}`

Изменить книгу по `slug`: `/api/books/{bookSlug}`

### DELETE  
Удалить книгу по `id`: `/api/books/{bookId}`

Удалить книгу по `slug`: `/api/books/{bookSlug}`

---

## 3. Авторы

### GET  
Получить всех авторов: `/api/authors`  

Получить автора по `id`: `/api/authors/{authorId}`

Получить автора по `slug`: `/api/authors/slug/{authorSlug}`

### POST  
Добавить автора: `/api/authors`

### PUT  
Изменить автора по `id`: `/api/authors/{authorId}`

### DELETE  
Удалить автора по `id`: `/api/authors/{authorId}`

### Книги автора  
### GET 

Получить все книги автора по `id`: `/api/authors/{authorId}/books` 

Получить все книги автора по `slug`: `/api/authors/slug/{authorSlug}/books`  

### POST 

Добавить связь книга–автор: `/api/authors/{authorId}/books`

### DELETE 

Удалить связь книга–автор: `/api/authors/{authorId}/books/{bookId}`


---

## 4. Жанры

### GET  
Получить все жанры: `/api/genres`  

Получить жанр по `id`: `/api/genres/{genreId}`  

Получить жанр по `slug`: `/api/genres/slug/{genreSlug}`

### POST  
Добавить жанр: `/api/genres`

### PUT  
Изменить жанр по `id: `/api/genres/{genreId}`

### DELETE  
Удалить жанр по `id`: `/api/genres/{genreId}`

### Книги по жанру  

### GET

Получить книги по жанру по `id`: `/api/genres/{genreId}/books`

Получить книги по жанру по `slug`: `/api/genres/slug/{genreSlug}/books`  

### POST 

Добавить книгу в жанр: `/api/genres/{genreId}/books/{bookId}`

### DELETE 

Удалить книгу из жанра: `/api/genres/{genreId}/books/{bookId}`

---

## 5. Издатели

### GET  

Получить всех издателей: `/api/publishers`  
Получить издателя по `id`: `/api/publishers/{publisherId}`  
Получить издателя по `slug`: `/api/publishers/slug/{publisherSlug}`

### POST  

Добавить издателя: `/api/publishers`

### PUT  

Изменить издателя по `id`: `/api/publishers/{publisherId}
`
### DELETE  

Удалить издателя по `id`: `/api/publishers/{publisherId}`

### Книги издателя  

### GET 

Получить книги издателя по `id`: `/api/publishers/{publisherId}/books`  

Получить книги издателя по `slug`: `/api/publishers/slug/{publisherSlug}/books`  

### POST 

Добавить книгу к издателю: `/api/publishers/{publisherId}/books/{bookId}`  

## DELETE 

Удалить книгу у издателя: `/api/publishers/{publisherId}/books/{bookId}`

---

## 6. Полки

### GET  

Получить все полки: `/api/shelves`  
Получить полку по `id`: `/api/shelves/{shelfId}`

### POST  

Добавить полку: `/api/shelves`

### PUT  

Изменить полку по `id`: `/api/shelves/{shelfId}`

### DELETE  

Удалить полку по `id`: `/api/shelves/{shelfId}`

## Книги на полке  

### GET 

Получить книги на полке: `/api/users/{userId}/shelves/{shelfId}/books`

### POST 

Добавить книгу на полку: `/api/users/{userId}/shelves/{shelfId}/books`  

### DELETE 

Убрать книгу с полки: `/api/users/{userId}/shelves/{shelfId}/books/{bookId}`

---

## 7. Теги

### GET  

Получить все теги: `/api/tags`  
Получить тег по `id`: `/api/tags/{tagId}`  
Получить тег по `slug`: `/api/tags/slug/{tagSlug}`

### POST  

Добавить тег: `/api/tags`

### PUT  

Изменить тег по id: `/api/tags/{tagId}`

### DELETE  

Удалить тег по id: `/api/tags/{tagId}`

### Книги по тегу  

### GET

Получить книги по тегу по id: `/api/tags/{tagId}/books`  

Получить книги по тегу по slug: `/api/tags/slug/{tagSlug}/books`  

### POST 

Добавить книгу к тегу: `/api/tags/{tagId}/books/{bookId}`  

### DELETE 

Удалить книгу из тега: `/api/tags/{tagId}/books/{bookId}`

---

## 8. Взаимодействия с книгой

## Оценки

### GET

Получить все оценки книги: `/api/books/{bookId}/ratings`  

### POST 

Добавить оценку: `/api/books/{bookId}/ratings`  

### PUT 

Изменить оценку: `/api/books/{bookId}/ratings`  

### DELETE 

Удалить оценку: `/api/books/{bookId}/ratings`

## Отзывы  

### GET

Получить все отзывы книги: `/api/books/{bookId}/reviews` 

Получить отзыв по `id`: `/api/reviews/{reviewId}`

### POST

Добавить отзыв: `/api/books/{bookId}/reviews`  

### PUT

Изменить отзыв: `/api/reviews/{reviewId}`  

### DELETE 

Удалить отзыв: `/api/reviews/{reviewId}`

### Реакции  

### GET

Получить все типы реакций: `/api/reactions`  

Получить реакции на книгу: `/api/books/{bookId}/reactions`  

### POST

Добавить реакцию на книгу по `id`: `/api/books/{bookId}/reactions`  

Добавить реакцию на книгу по `slug`: `/api/books/{bookSlug}/reactions`  

### DELETE

Удалить реакцию на книгу по `id`: `/api/books/{bookId}/reactions/{reactionId}` 

Удалить реакцию на книгу по `slug`: `/api/books/{bookId}/reactions/{reactionId}`

---

## 9. Социальные функции

### Подписки на авторов

### GET

Получить подписки пользователя: `/api/users/{userId}/following`

### POST 

Подписаться на автора: `/api/authors/{authorId}/followers`

### DELETE 

Отписаться от автора: `/api/authors/{authorId}/followers/{userId}`

## Посты и комментарии  

### GET 

Получить все посты: `/api/posts`

Получить пост по `id`: `/api/posts/{postId}`  

Получить все комментарие к посту: `/api/posts/{postId}/comments`  

### POST

Добавить пост: `/api/posts`  

Добавить комментарий: `/api/posts/{postId}/comments`

### DELETE

Удалить пост по `id`: `/api/posts/{postId}`  
 
Удалить комментарий по `id`: `/api/comments/{commentId}`

--- 

# TODO
- Добавить примеры запросов/ответов