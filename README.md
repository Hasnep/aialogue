# AIalogue

## Running

Export an OpenAI API key as an environment variable:

```shell
export OPEN_AI_API_KEY=...
```

Build and run the Docker image

```shell
docker build --tag=aialogue .
docker run --env OPEN_AI_API_KEY=$OPEN_AI_API_KEY --publish 8080 aialogue
```

Access the app in your browser at [localhost:8080](http://localhost:8080).
