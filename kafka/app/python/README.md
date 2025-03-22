# Installation

```bash
python3 -m venv venv
pip install
```

or

```bash
python3 -m venv venv
pip install confluent-kafka
pip freeze > requirements.txt

source venv/bin/activate
```

# Run

To start the consumer, run

```bash
python3 consumer.py
```

To send messages to consumer, run

```bash
python3 producer.py
```
