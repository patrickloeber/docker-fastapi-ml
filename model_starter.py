from transformers import ViltProcessor, ViltForQuestionAnswering
import requests
from PIL import Image

# 470MB
processor = ViltProcessor.from_pretrained("dandelin/vilt-b32-finetuned-vqa")
model = ViltForQuestionAnswering.from_pretrained("dandelin/vilt-b32-finetuned-vqa")

# prepare image + question
url = "http://images.cocodataset.org/val2017/000000039769.jpg"
image = Image.open(requests.get(url, stream=True).raw)

text = "How many cats are there?"

# prepare inputs
encoding = processor(image, text, return_tensors="pt")

# TODO: inspect encoding

# forward pass
outputs = model(**encoding)
logits = outputs.logits
idx = logits.argmax(-1).item()

# TODO: inspect outputs and test how to get the answer
#print(idx)
#print()
#print(model.config.id2label))

print("Predicted answer:", model.config.id2label[idx])

# TODO: put above code into a function that accepts image and text as input