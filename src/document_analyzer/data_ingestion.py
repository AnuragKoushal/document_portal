import os
import fitz
from datetime import datetime
from logger import CustomLogger
from exception.custom_exception import DocumentPortalException



class DocumentHandler:
    """
    Handles pdf saving and reading operations.
    """
    def __init__(self,data_dir = None, session_id = None):
        try:
            self.log = CustomLogger().get_logger(__name__)
            self.data_dir = data_dir or os.getenv(
                "DATA_STORAGE_PATH",
                os.path.join(os.getcwd(), "data", "document_analysis")
            )
            self.session_id = session_id or datetime.now().strftime("%Y%m%d_%H%M%S")
            
            #create base session directory
            self.session_path = os.path.join(self.data_dir, self.session_id)
            os.makedirs(self.session_path, exist_ok=True)
            self.log.info(f"Session directory created at {self.session_path}")
            
        except Exception as e:
            self.log.error(f"Error initializing DocumentHandler: {e}")
            raise DocumentPortalException("Error in DocumentHandler initialization", e) from e
        
    def save_pdf(self):
        pass
    
    def read_pdf(self):
        pass