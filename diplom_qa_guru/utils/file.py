def abs_path_from_project(relative_path: str):
    import diplom_qa_guru
    from pathlib import Path

    return (
        Path(diplom_qa_guru.__file__)
        .parent.parent.joinpath(relative_path)
        .absolute()
        .__str__()
    )
