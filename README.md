## Installation

### Using Docker (Recommended)

1. Clone the repository:
```bash
git clone git@github.com:Viktopia/notipus.git
cd notipus
```

2. Build the Docker image:
```bash
docker build -t notipus .
```

3. Run the container with your environment variables:
```bash
docker run -d \
  -p 8080:8080 \
  -e SLACK_WEBHOOK_URL=your_slack_webhook_url \
  -e CHARGIFY_WEBHOOK_SECRET=your_chargify_webhook_secret \
  -e SHOPIFY_WEBHOOK_SECRET=your_webhook_secret \
  notipus
```
