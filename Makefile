### Getting started
.PHONY: help

# help auto generates a help message from the Makefile comments
# - Use ## to add a description to a target and include it in the help output
# - Use ### to add a section header in the help output
help: ## List available commands
	@awk '\
		/^### / { \
			sub(/^### /, ""); \
			printf "\n\033[1;35m%s\033[0m\n", $$0; \
			next \
		} \
		/^[a-zA-Z0-9_.-]+:.*## / { \
			split($$0, parts, ":.*## "); \
			printf "  \033[36m%-20s\033[0m %s\n", parts[1], parts[2]; \
		}' $(MAKEFILE_LIST)

### Running
.PHONY: run-duckdb
run-duckdb: ## Launch DuckDB local UI with hived dataset
	@duckdb src/hived_data_eng/defs/data/hived.duckdb --ui

