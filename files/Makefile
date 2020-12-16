.PHONY: test
all: extract transform load

post_staging:
	echo "Posting organizations...."
	python3 ./post_loop.py --env ".staging."

post_demo:
	echo "Posting organizations...."
	python3 ./post_loop.py --env ".demo."

post_prod:
	echo "Posting organizations...."
	python3 ./post_loop.py --env "."

get_elastic_staging:
	echo "Getting elasticdata...."
	python3 ./get_elastic.py --host "" --index /dcat --env staging

get_elastic_demo:
	echo "Getting elasticdata...."
	python3 ./get_elastic.py --host "" --index /dcat --env demo

get_elastic_prod:
	echo "Getting elasticdata...."
	python3 ./get_elastic.py --host "https://data.norge.no" --index "/" --env prod

put_staging:
	echo "Putting organization preflabel...."
	python3 ./put_loop.py --env ".staging."

put_demo:
	echo "Putting organization prefLabel...."
	python3 ./put_loop.py --env ".demo."

put_prod:
	echo "Putting organization prefLabel...."
	python3 ./put_loop.py --env ".prod."

clean:
	rm ./tmp/*.json
