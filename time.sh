#!/bin/bash

for _ in {1..3}
do
  echo "request"
  curl http://localhost:8000/polls/ &
done
wait

# time curl http://localhost:8000/polls/
