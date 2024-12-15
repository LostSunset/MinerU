from typing import Callable

from abc import ABC, abstractmethod

from magic_pdf.data.data_reader_writer import DataWriter
from magic_pdf.data.dataset import Dataset
from magic_pdf.pipe.operators import PipeResult


__use_inside_model__ = True
__model_mode__ = "full"


class InferenceResultBase(ABC):

    @abstractmethod
    def __init__(self, inference_results: list, dataset: Dataset):
        """Initialized method.

        Args:
            inference_results (list): the inference result generated by model
            dataset (Dataset): the dataset related with model inference result
        """
        self._infer_res = inference_results
        self._dataset = dataset

    @abstractmethod
    def draw_model(self, file_path: str) -> None:
        """Draw model inference result.

        Args:
            file_path (str): the output file path
        """
        pass

    @abstractmethod
    def dump_model(self, writer: DataWriter, file_path: str):
        """Dump model inference result to file.

        Args:
            writer (DataWriter): writer handle
            file_path (str): the location of target file
        """
        pass

    @abstractmethod
    def get_infer_res(self):
        """Get the inference result.

        Returns:
            list: the inference result generated by model
        """
        pass

    @abstractmethod
    def apply(self, proc: Callable, *args, **kwargs):
        """Apply callable method which.

        Args:
            proc (Callable): invoke proc as follows:
                proc(inference_result, *args, **kwargs)

        Returns:
            Any: return the result generated by proc
        """
        pass

    @abstractmethod
    def pipe_auto_mode(
        self,
        imageWriter: DataWriter,
        start_page_id=0,
        end_page_id=None,
        debug_mode=False,
        lang=None,
    ) -> PipeResult:
        """Post-proc the model inference result.
            step1: classify the dataset type
            step2: based the result of step1, using `pipe_txt_mode` or `pipe_ocr_mode`

        Args:
            imageWriter (DataWriter): the image writer handle
            start_page_id (int, optional): Defaults to 0. Let user select some pages He/She want to process
            end_page_id (int, optional):  Defaults to the last page index of dataset. Let user select some pages He/She want to process
            debug_mode (bool, optional): Defaults to False. will dump more log if enabled
            lang (str, optional): Defaults to None.

        Returns:
            PipeResult: the result
        """
        pass

    @abstractmethod
    def pipe_txt_mode(
        self,
        imageWriter: DataWriter,
        start_page_id=0,
        end_page_id=None,
        debug_mode=False,
        lang=None,
    ) -> PipeResult:
        """Post-proc the model inference result, Extract the text using the
        third library, such as `pymupdf`

        Args:
            imageWriter (DataWriter): the image writer handle
            start_page_id (int, optional): Defaults to 0. Let user select some pages He/She want to process
            end_page_id (int, optional):  Defaults to the last page index of dataset. Let user select some pages He/She want to process
            debug_mode (bool, optional): Defaults to False. will dump more log if enabled
            lang (str, optional): Defaults to None.

        Returns:
            PipeResult: the result
        """
        pass

    @abstractmethod
    def pipe_ocr_mode(
        self,
        imageWriter: DataWriter,
        start_page_id=0,
        end_page_id=None,
        debug_mode=False,
        lang=None,
    ) -> PipeResult:
        pass
