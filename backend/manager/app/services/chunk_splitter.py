import math


class ChunkSplitter:
    DEFAULT_CHUNK_SIZE = 10 * 1024 * 1024  # 10 MB

    @staticmethod
    def split(
        file_size: int,
        chunk_size: int = DEFAULT_CHUNK_SIZE,
    ) -> list[tuple[int, int]]:
        """
        Returns:
            [
                (start_byte, end_byte),
                ...
            ]
        """

        chunks: list[tuple[int, int]] = []

        total_chunks = math.ceil(file_size / chunk_size)

        for index in range(total_chunks):
            start = index * chunk_size
            end = min(start + chunk_size - 1, file_size - 1)

            chunks.append((start, end))

        return chunks
