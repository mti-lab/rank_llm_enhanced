import json
import logging
from typing import Dict, Optional

logger = logging.getLogger(__name__)


class PreprocessedQueryLoader:
    """Load and manage preprocessed query information for enhanced reranking"""
    
    def __init__(self, preprocess_file_path: str):
        """
        Initialize the preprocessed query loader
        
        Args:
            preprocess_file_path: Path to the JSON file containing preprocessed queries
        """
        self.preprocessed_queries = {}
        
        try:
            with open(preprocess_file_path, 'r', encoding='utf-8') as f:
                queries = json.load(f)
                
            # Create a mapping from topic_id to query info
            for query_info in queries:
                topic_id = query_info.get('topic_id')
                if topic_id:
                    self.preprocessed_queries[topic_id] = query_info
                    
            logger.info(f"Loaded {len(self.preprocessed_queries)} preprocessed queries")
            
        except Exception as e:
            logger.error(f"Failed to load preprocessed queries from {preprocess_file_path}: {e}")
            raise
    
    def get_preprocessing_info(self, topic_id: str) -> Optional[Dict]:
        """
        Get preprocessing information for a specific topic ID
        
        Args:
            topic_id: The topic/query ID to look up
            
        Returns:
            Dictionary containing preprocessing info if found, None otherwise
        """
        # Try exact match first
        if topic_id in self.preprocessed_queries:
            return self.preprocessed_queries[topic_id]
        
        # Try with different formats (in case of ID format mismatch)
        # Remove leading zeros if present
        normalized_id = topic_id.lstrip('0')
        if normalized_id in self.preprocessed_queries:
            return self.preprocessed_queries[normalized_id]
            
        # Try adding prefix if not present
        if not topic_id.startswith('2024-'):
            prefixed_id = f"2024-{topic_id}"
            if prefixed_id in self.preprocessed_queries:
                return self.preprocessed_queries[prefixed_id]
        
        logger.debug(f"No preprocessing info found for topic_id: {topic_id}")
        return None
    
    def has_preprocessing_info(self, topic_id: str) -> bool:
        """Check if preprocessing info exists for a topic ID"""
        return self.get_preprocessing_info(topic_id) is not None