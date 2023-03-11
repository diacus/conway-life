from scene import load_scene_by_name


def test_scene_is_loaded_by_name():
    scene = load_scene_by_name("space-ships")

    assert isinstance(scene, dict)
