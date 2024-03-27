help: ## Show help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

# Postgres database
local_db: ## Starts a local postgres database
	$(engine) run --platform linux/$(arch) -d \
	--name postgres-test \
	-e POSTGRES_PASSWORD=${pass} \
	-e POSTGRES_DB=mytestdb \
	-p 5432:5432 \
	postgres:latest

pre_commit_update: ## Update pre-commit hooks
	pre-commit install
	pre-commit autoupdate

lint: ## Run pre-commit commands
	pre-commit run --all-files
