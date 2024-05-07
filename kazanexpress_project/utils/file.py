def abs_path_from_project(relative_path: str):
    import kazanexpress_project
    from pathlib import Path

    return (
        Path(kazanexpress_project.__file__)
        .parent.parent.joinpath(relative_path)
        .absolute()
        .__str__()
    )
