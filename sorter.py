from pathlib import Path
import os.path

from threading import Thread
import os

PATH = Path(r"C:\Users\Admin\Desktop\garvbige")
NEW_DIRECTORY = ("images", "video", "documents", "archive", "unknown")
THREADS = []

list_images = list()
list_video = list()
list_documents = list()
list_archive = list()
list_unknown = list()



def list_files(path: Path, ):
    images = (".jpeg", ".png", ".jpg", ".svg")
    video = (".avi", ".mp4", ".mov", ".mkv")
    documents = (".doc", ".docx", ".txt", ".pdf", ".xlsx", ".pptx")
    archive = ('.zip', ".gz", ".tar")

    for file in path.iterdir():
        if file.is_dir():
            if not file.name in NEW_DIRECTORY:
                thread = Thread(target=list_files, args=(file,))
                thread.start()
                THREADS.append(thread)
        elif file.suffix in images:
            list_images.append(file)
        elif file.suffix in video:
            list_video.append(file)
        elif file.suffix in documents:
            list_documents.append(file)
        elif file.suffix in archive:
            list_archive.append(file)
        else:
            list_unknown.append(file)


def move_to_image_folder(path: Path, list_images: list[str]):
    new_folder_images = f"{path}\\images"

    for file_path in list_images:
        path_to_file = Path(file_path)
        new_path = f"{new_folder_images}\\{path_to_file.name}"
        os.replace(file_path, new_path)


def move_to_video_folder(path: Path, list_video: list[str]):
    new_folder_video = f"{path}\\video"
    for file_path in list_video:
        path_to_file = Path(file_path)
        new_path = f"{new_folder_video}\\{path_to_file.name}"
        os.replace(file_path, new_path)


def move_to_document_folder(path: Path, list_documents: list[str]):
    new_folder_documetn = f"{path}\\document"
    for file_path in list_documents:
        path_to = Path(file_path)
        new_path = f"{new_folder_documetn}\\{path_to.name}"
        os.replace(file_path, new_path)


def move_to_archive_folder(path: Path, list_archive: list[str]):
    new_folder_archive = f"{path}\\archive"

    for file_path in list_archive:
        path_to = Path(file_path)
        new_path = f"{new_folder_archive}\\{path_to.name}"
        os.replace(file_path, new_path)


def move_to_unknown_folder(path: Path, list_unknown: list[str]):
    new_folder_unknown = f"{path}\\unknown"
    for file_path in list_unknown:
        path_to = Path(file_path)
        new_path = f"{new_folder_unknown}\\{path_to.name}"
        os.replace(file_path, new_path)


def move_to_directory():
    thread_move_images = Thread(target=move_to_image_folder, args=(PATH, list_images))
    thread_move_images.start()
    thread_move_video = Thread(target=move_to_video_folder, args=(PATH, list_video))
    thread_move_video.start()
    thread_move_documents = Thread(target=move_to_document_folder, args=(PATH, list_documents))
    thread_move_documents.start()
    thread_move_archive = Thread(target=move_to_archive_folder, args=(PATH, list_archive))
    thread_move_archive.start()
    thread_move_unknown = Thread(target=move_to_image_folder, args=(PATH, list_unknown))
    thread_move_unknown.start()
    thread_move_images.join()
    thread_move_video.join()
    thread_move_documents.join()
    thread_move_archive.join()
    thread_move_unknown.join()


def create_directory(path: Path, new_directory: tuple):
    for directory in new_directory:
        new_folder = f"{path}\\{directory}"

        if not os.path.exists(new_folder):
            os.mkdir(new_folder)


if __name__ == "__main__":
    create_directory(PATH, NEW_DIRECTORY)
    list_files(PATH)
    [el.join() for el in THREADS]
    move_to_directory()
    print("Successfully sorted")
