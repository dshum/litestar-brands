FROM node:22-alpine

WORKDIR /app

COPY package.json package.json
COPY package-lock.json package-lock.json
RUN npm install

ENV PATH /app/node_modules/.bin:$PATH
ENV PORT 5000

COPY . .
RUN npm run build
RUN npm prune --production

EXPOSE 5000

CMD [ "node", "build" ]