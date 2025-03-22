<p align="center">
<img src="../.github/assets/k6.svg" align="center" width="200" />
    <h1 align="center">k6</h1>
    <p align="center">Playground & starter</p>
</p>

## Documentation

<a href="https://k6.io/">Official website</a>

## Run it

```bash
docker compose up -d
```

## Run tests

```bash
k6 run --out dashboard=export=test-report.html runners/availability.js
```
