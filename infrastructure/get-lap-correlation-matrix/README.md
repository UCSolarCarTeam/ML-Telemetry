# Commands

From View Push Commands:
<https://ca-central-1.console.aws.amazon.com/ecr/repositories/private/602361116849/get-lap-correlation-matrix?region=ca-central-1>

```bash
aws ecr get-login-password --region ca-central-1 | docker login --username AWS --password-stdin 602361116849.dkr.ecr.ca-central-1.amazonaws.com

docker build -t get-lap-correlation-matrix .

docker tag get-lap-correlation-matrix:latest 602361116849.dkr.ecr.ca-central-1.amazonaws.com/get-lap-correlation-matrix:latest

docker push 602361116849.dkr.ecr.ca-central-1.amazonaws.com/get-lap-correlation-matrix:latest
```
