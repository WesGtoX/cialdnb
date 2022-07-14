build:
	@echo "--> Build Docker image as run_cialdnb."
	docker build . -t run_cialdnb

run:
	@echo "--> Running run_cialdnb image."
	cat websites.txt | docker run -i run_cialdnb
