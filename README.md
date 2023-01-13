# rgb-system

## How to build application 🛠️

The only thing you will need should be **Docker** 🐋

```bash
# To build all the backend:
docker-compose up -d --build

# To build all the app including front-end:
docker-compose --profile=all up -d --build
```

## Time to clean up ? 🧽

```bash
docker-compose down -v --profile=all --rmi all
```
