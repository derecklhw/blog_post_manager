# Blog Post Manager

## Description

This project is a full stack blog post manager that allows users to add, view, update, and delete blog posts ensuring a smooth and interactive user experience while following best practices in both frontend and
backend development.

## Architecture

![Architecture](./images/architecture.png)

## Run

Build and run the multi-container application with its dependencies.

```bash
docker-compose up -d --build
```

After running the command, the application will be available at `http://localhost:3000`.

### Testing

Run the following command to run the tests.

```bash
docker exec -it blog_post_manager-api-1 pytest tests/.
```
