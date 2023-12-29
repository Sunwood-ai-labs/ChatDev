docker-compose exec chatdev /bin/bash

pip install pytk

--config

python3 run.py --task "[description_of_your_idea]" --name "[project_name]"

python3 run.py --task "[description_of_your_idea]" --name "[project_name]" --model "nekomata-7b-instruction-Q4_K_M"

python run.py --task "Create a simple japan clock in Python" --name "clockJP2" --config "DefaultJP"
python run.py --task "Create a simple clock in Japanese with Python" --name "clockJP2" --config "DefaultJP"

python3 run.py --task "Create a simple clock in Japanese with Python" --name "NEKOclockJP3" --config "DefaultJP2"  --model "nekomata-7b-instruction-Q4_K_M"

python3 run.py --task "Create a simple clock in Japanese with Python" --name "NEKOclockJP3" --config "DefaultJP2"  --model "nekomata-14b-instruction-Q4_K_M"

python3 run.py --task "Create a simple clock with Python" --name "DEEPclockJP3" --config "DefaultJP2"  --model "nekomata-14b-instruction-Q4_K_M"
python3 run.py --task "Create a simple clock with Python" --name "DEEPclock" --config "Default"  --model "nekomata-14b-instruction-Q4_K_M"

/mnt/e/Prj/ChatDev
docker-compose exec chatdev /bin/bash
pip install openai==0.28

docker network create chatdev_shared_network


http://localhost:1234/v1/models
http://host.docker.internal:1234/v1/models

curl http://host.docker.internal:1234/v1/chat/completions \
-H "Content-Type: application/json" \
-d '{ 
  "messages": [ 
    { "role": "system", "content": "Always answer in rhymes." },
    { "role": "user", "content": "Introduce yourself." }
  ], 
  "temperature": 0.7, 
  "max_tokens": -1,
  "stream": false
}'

curl http://host.docker.internal:1234/v1/chat/completions \
-H "Content-Type: application/json" \
-d '{ 
  "messages": [ 
    { "role": "system", "content": "Always answer in rhymes." },
    { "role": "user", "content": "Introduce yourself." }
  ], 
  "temperature": 0.7, 
  "max_tokens": -1,
  "stream": false
}'