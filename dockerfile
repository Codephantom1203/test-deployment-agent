
## 🐳 **Dockerfile Content:**

```docke-srelim

WORKDIR /app

COPY retxt.
RUN pip insall -r requiements.txt
X
COPY . .

EXDPOSE 5000

CMD["python", "y"]
