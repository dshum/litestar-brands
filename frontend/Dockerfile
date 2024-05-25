FROM node:22-alpine

WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

COPY . .
EXPOSE 5000

CMD [ "npm", "run", "dev" ]