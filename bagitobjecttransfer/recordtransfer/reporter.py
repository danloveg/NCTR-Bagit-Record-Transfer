''' Facilitates writing reports to disk '''
import logging
from pathlib import Path

from django.utils import timezone

from recordtransfer.exceptions import FolderNotFoundError


LOGGER = logging.getLogger(__name__)


def write_report(storage_folder: str, document: str, doc_extension: str, doc_identifier=None):
    ''' Write a report string to a file.

    Args:
        storage_folder (str): The folder to store the document in
        document (str): The string containing the contents of the document
        doc_extension (str): The file extension to use for the outputted report
        doc_identifier (str): A string identifying the document. If no string is supplied, the time
            will be used to identify the document. The identifier is used as part of the filename

    Returns:
        (dict): 'report_created' is True if the document was written, and False if not.
            'report_location' is the path to the written report if it was written, None otherwise.
            'time_created' is the time the report was written if it was written, None otherwise.
    '''
    if not Path(storage_folder).exists():
        LOGGER.error(msg=('Reporter: Could not find report storage folder "%s"' % storage_folder))
        raise FolderNotFoundError(f'Could not find folder "{storage_folder}"')

    current_time = timezone.now()
    identifier = doc_identifier or current_time.strftime(r'%Y%m%d_%H%M%S')

    report_path = _get_new_report_path(storage_folder, identifier, doc_extension)
    report_created = False
    try:
        with open(report_path, 'w', encoding='utf8') as file_pointer:
            file_pointer.write(document)
        LOGGER.info(msg=('Report created at "%s"' % report_path))
        report_created = True
    except IOError as exc:
        LOGGER.info(msg=('Report creation failed: %s' % str(exc)))
    return {
        'report_created': report_created,
        'report_location': str(report_path) if report_created else None,
        'time_created': current_time if report_created else None,
    }

def _get_new_report_path(storage_folder: str, identifier: str, extension: str):
    storage_folder_path = Path(storage_folder)
    if not Path(storage_folder_path).exists():
        raise FolderNotFoundError(f'Could not find folder "{storage_folder}"')
    report_path = storage_folder_path / f'Report_{identifier}.{extension}'
    increment = 1
    while report_path.exists():
        report_path = storage_folder_path / f'Report_{identifier} ({increment}).{extension}'
        increment += 1
    return report_path
