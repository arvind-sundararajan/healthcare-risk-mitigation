```json
{
    "memory/short_term_memory.py": {
        "content": "
import logging
from typing import List, Dict
from openai import OpenAI
from traceloop.sdk import Traceloop
from langsmith import StateGraph
from gensim import corpora

logger = logging.getLogger(__name__)

class ShortTermMemory:
    def __init__(self, non_stationary_drift_index: float, stochastic_regime_switch: bool):
        """
        Initialize the ShortTermMemory class.

        Args:
        - non_stationary_drift_index (float): The index of non-stationary drift.
        - stochastic_regime_switch (bool): Whether to use stochastic regime switch.

        Returns:
        - None
        """
        self.non_stationary_drift_index = non_stationary_drift_index
        self.stochastic_regime_switch = stochastic_regime_switch
        self.state_graph = StateGraph()

    def ingest_traces(self, traces: List[Dict]) -> None:
        """
        Ingest traces into the short-term memory.

        Args:
        - traces (List[Dict]): A list of traces.

        Returns:
        - None
        """
        try:
            for trace in traces:
                self.state_graph.add_node(trace['node_id'], trace['node_data'])
                logger.info(f'Ingested trace {trace["node_id"]}')
        except Exception as e:
            logger.error(f'Error ingesting traces: {e}')

    def update_state(self, new_state: Dict) -> None:
        """
        Update the state of the short-term memory.

        Args:
        - new_state (Dict): The new state.

        Returns:
        - None
        """
        try:
            self.state_graph.update_node(new_state['node_id'], new_state['node_data'])
            logger.info(f'Updated state {new_state["node_id"]}')
        except Exception as e:
            logger.error(f'Error updating state: {e}')

    def query_state(self, query: str) -> List[Dict]:
        """
        Query the state of the short-term memory.

        Args:
        - query (str): The query.

        Returns:
        - List[Dict]: A list of states matching the query.
        """
        try:
            results = self.state_graph.query_nodes(query)
            logger.info(f'Queried state {query}')
            return results
        except Exception as e:
            logger.error(f'Error querying state: {e}')
            return []

def main():
    # Initialize the short-term memory
    short_term_memory = ShortTermMemory(non_stationary_drift_index=0.5, stochastic_regime_switch=True)

    # Initialize the Traceloop client
    Traceloop.init()

    # Initialize the OpenAI client
    openai_client = OpenAI()

    # Create a completion
    completion = openai_client.chat.completions.create(model='gpt-4o', messages=[{'role': 'user', 'content': 'Hello, how are you?'}])

    # Ingest the completion into the short-term memory
    short_term_memory.ingest_traces([{'node_id': 'completion', 'node_data': completion}])

    # Update the state of the short-term memory
    short_term_memory.update_state({'node_id': 'completion', 'node_data': {'response': 'I am good, thank you!'}})

    # Query the state of the short-term memory
    results = short_term_memory.query_state('completion')

    # Print the results
    print(results)

if __name__ == '__main__':
    main()
",
        "commit_message": "feat: implement specialized short_term_memory logic"
    }
}
```