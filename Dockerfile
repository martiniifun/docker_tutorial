# 파이썬 3.11 환경
FROM python:3.11-slim

WORKDIR /app

# 시스템 의존성 설치 (Reflex 및 내부 도구 작동용)
RUN apt-get update && apt-get install -y \
    unzip \
    curl \
    && rm -rf /var/lib/apt/lists/*

# 파이썬 패키지 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 소스 코드 복사
COPY . .

# Reflex 초기화 및 빌드
RUN reflex init
RUN reflex export --frontend-only

# 포트 개방
EXPOSE 3000 8000

# 프로덕션 모드로 실행
CMD ["reflex", "run", "--env", "prod"]