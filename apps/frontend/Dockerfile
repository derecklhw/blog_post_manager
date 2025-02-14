FROM node:18.18.2-alpine

WORKDIR /frontend

EXPOSE 3000

RUN --mount=type=bind,source=package.json,target=package.json \
    --mount=type=bind,source=package-lock.json,target=package-lock.json \
    --mount=type=cache,target=/root/.npm \
    npm ci --include=dev

COPY . .

CMD ["npm", "run", "dev"]