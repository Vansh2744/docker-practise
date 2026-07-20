FROM oven/bun:canary-debian

WORKDIR /app

COPY *.json .
COPY bun.lock .
RUN bun install

COPY . .

CMD ["bun", "run", "index.ts"]