from backend.manager.app.services.chunk_splitter import ChunkSplitter


def test_chunk_splitter():
    chunks = ChunkSplitter.split(
        file_size=25 * 1024 * 1024,
        chunk_size=10 * 1024 * 1024,
    )

    assert chunks == [
        (0, 10485759),
        (10485760, 20971519),
        (20971520, 26214399),
    ]
