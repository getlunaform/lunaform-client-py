##################
# Client targets #
##################

GOROOT?=${HOME}/go
SRC_YAML?=${GOROOT}/src/github.com/getlunaform/lunaform/swagger.yml

PARENT_DIR=$(dir ${CURDIR})
CUR_DIR_NAME=$(notdir ${CURDIR})

clean:
	find ${CURDIR} -name "*.js" -delete && \
	find ${CURDIR} -name ".DS_STORE" -delete && \
	find ${CURDIR} -type d -empty -delete

generate:
	swagger-codegen generate \
		-i $(SRC_YAML) \
		-l python \
		--api-package lunaform \
		-o ${CURDIR} -v
