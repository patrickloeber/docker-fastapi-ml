Model: https://huggingface.co/dandelin/vilt-b32-finetuned-vqa

STEP: Run `docker init`

```
docker init
```

STEP: Select Python image and use this command during docker init
```
CMD uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

STEP: Remove `-slim` and add this to Dockerfile (Needed to install transformers)

```
# Install Rust compiler
RUN curl https://sh.rustup.rs -sSf | bash -s -- -y
ENV PATH="/root/.cargo/bin:${PATH}"
```

STEP: Remove the custom user from the Dockerfile to simplify, because HF needs write permissions to download and save the model.

STEP: Add volume to `compose.yaml`:

STEP Run `docker compose up --build`

STEP: Attach VS Code to running container

```
    volumes:
      - .:/app
```

## Examples

- file: cats.jpeg
  
  text: How many cats are there?

- file: tiger.jpeg

  text: What's the animal doing?

- file: palace.jpeg

  text: What is on top of the building?