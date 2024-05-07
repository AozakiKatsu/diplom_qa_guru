def abs_path_from_project(relative_path: str):
    import tests_kazanexpress
    from pathlib import Path

    return (
        Path(tests_kazanexpress.__file__)
        .parent.parent.joinpath(relative_path)
        .absolute()
        .__str__()
    )
