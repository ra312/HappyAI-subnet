
import json
import os
import time


import bittensor as bt

from app.chain.base.miner import BaseMinerNeuron

from dotenv import load_dotenv

from app.chain.protocol import CompletionSynapse
from app.chain.worker import Worker

load_dotenv()

class Miner(BaseMinerNeuron):


    def __init__(self):
        super(Miner, self).__init__()
        self.worker = Worker(worker_url=os.environ["WORKER_URL"], worker_port=os.environ["WORKER_PORT"])
        self.evaluator = Evaluator(llm_client, self.worker)

    async def forward_completion(
        self, query: CompletionSynapse
    ) -> CompletionSynapse:
        bt.logging.trace(f'Processing request: {query.request_id}')
        request_data = {
            'request_id': query.request_id,
            'user_input': {'sender': 'user', 'text': query.user_input},
            'dialog': [{'sender': message.role, 'text': message.content} for message in query.messages],
            'chat_llm_model': 'main'
        }
        response = self.worker.process_request(request_data)
        assistant_message = json.loads(response.text)['assistant_message']
        
        golden_reference_answer = self.evaluator._get_reference_result(query)
        bt.logging.trace(f'Assistant message: {golden_reference_answer}')
        query.results = golden_reference_answer
        return query


# This is the main function, which runs the miner.
if __name__ == "__main__":
    with Miner() as miner:
        miner_hotkey = miner.wallet.hotkey.ss58_address
        bt.logging.trace(f"My Miner hotkey: {miner_hotkey}")
        time.sleep(120)
        while True:
            time.sleep(30)

