FROM node:22-alpine

WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH
ENV PORT 5000

COPY . ./

EXPOSE 5000

CMD [ "npm", "run", "dev" ]