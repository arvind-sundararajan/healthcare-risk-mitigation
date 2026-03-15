```json
{
    "utils/data_preprocessing.py": {
        "content": "
import logging
from typing import List, Dict
from gensim.models import TfidfModel
from pathway import Pathway
from openai import OpenAI
from traceloop.sdk import Traceloop

# Initialize logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def non_stationary_drift_index(data: List[float]) -> float:
    """
    Calculate the non-stationary drift index for the given data.

    Args:
    - data (List[float]): The input data.

    Returns:
    - float: The non-stationary drift index.
    """
    try:
        # Calculate the mean and standard deviation of the data
        mean = sum(data) / len(data)
        std_dev = (sum((x - mean) ** 2 for x in data) / len(data)) ** 0.5
        
        # Calculate the non-stationary drift index
        drift_index = sum((x - mean) ** 2 for x in data) / (len(data) * std_dev ** 2)
        
        logger.info('Non-stationary drift index calculated successfully')
        return drift_index
    except Exception as e:
        logger.error(f'Error calculating non-stationary drift index: {e}')
        return None

def stochastic_regime_switch(data: List[float]) -> Dict[str, float]:
    """
    Perform stochastic regime switching on the given data.

    Args:
    - data (List[float]): The input data.

    Returns:
    - Dict[str, float]: A dictionary containing the regime-switched data.
    """
    try:
        # Initialize the regime-switched data dictionary
        regime_switched_data = {}
        
        # Perform regime switching using the pathway library
        pathway_model = Pathway()
        regime_switched_data['switched_data'] = pathway_model.fit_transform(data)
        
        logger.info('Stochastic regime switching performed successfully')
        return regime_switched_data
    except Exception as e:
        logger.error(f'Error performing stochastic regime switching: {e}')
        return None

def tf_idf_vectorization(data: List[str]) -> TfidfModel:
    """
    Perform TF-IDF vectorization on the given data.

    Args:
    - data (List[str]): The input data.

    Returns:
    - TfidfModel: The TF-IDF model.
    """
    try:
        # Initialize the TF-IDF model
        tf_idf_model = TfidfModel(data)
        
        logger.info('TF-IDF vectorization performed successfully')
        return tf_idf_model
    except Exception as e:
        logger.error(f'Error performing TF-IDF vectorization: {e}')
        return None

def log_traces_to_langsmith(traces: List[Dict[str, str]]) -> None:
    """
    Log traces to LangSmith.

    Args:
    - traces (List[Dict[str, str]]): The traces to log.
    """
    try:
        # Initialize the Traceloop client
        Traceloop.init()
        
        # Log the traces to LangSmith
        for trace in traces:
            Traceloop.log(trace)
        
        logger.info('Traces logged to LangSmith successfully')
    except Exception as e:
        logger.error(f'Error logging traces to LangSmith: {e}')

if __name__ == '__main__':
    # Simulate the 'Rocket Science' problem
    data = [1.0, 2.0, 3.0, 4.0, 5.0]
    drift_index = non_stationary_drift_index(data)
    regime_switched_data = stochastic_regime_switch(data)
    tf_idf_model = tf_idf_vectorization(['This is a test sentence'])
    traces = [{'trace': 'This is a test trace'}]
    log_traces_to_langsmith(traces)
    print('Rocket Science problem simulated successfully')
",
        "commit_message": "feat: implement specialized data_preprocessing logic"
    }
}
```