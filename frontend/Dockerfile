FROM oven/bun:canary-debian

WORKDIR /app

COPY tsconfig*.json .
COPY bun.lock .
COPY package.json .
RUN bun install

COPY . .

EXPOSE 5173

CMD ["bun", "run", "dev", "--", "--host"]