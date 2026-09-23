import pandas as pd


def test_segments_cover_students_and_preserve_the_five_groups():
    source = pd.read_csv("data/snsdata.csv")
    segmented = pd.read_csv("submission/segmented.csv")
    sizes = pd.read_csv("submission/cluster_sizes.csv")

    assert len(segmented) == len(source)
    assert set(segmented["cluster"]) == {0, 1, 2, 3, 4}
    assert "segment" not in segmented.columns
    assert sizes["cluster"].tolist() == [0, 1, 2, 3, 4]
    assert sizes["n"].sum() == len(source)
    assert sizes["percentage"].sum().round(2) == 100.0


def test_persisted_profiles_are_evidence_not_predefined_interpretations():
    top_interests = pd.read_csv("submission/top_interests.csv")
    cluster_profiles = pd.read_csv("submission/cluster_profiles.csv")
    gender_profiles = pd.read_csv("submission/gender_profiles.csv")
    gradyear_profiles = pd.read_csv("submission/gradyear_profiles.csv")

    assert top_interests.groupby("cluster").size().to_dict() == {
        0: 6,
        1: 6,
        2: 6,
        3: 6,
        4: 6,
    }
    assert top_interests["interest"].notna().all()
    assert set(cluster_profiles["cluster"]) == {0, 1, 2, 3, 4}
    assert cluster_profiles["n"].sum() == 30000
    assert set(gender_profiles["cluster"]) == {0, 1, 2, 3, 4}
    assert set(gradyear_profiles["cluster"]) == {0, 1, 2, 3, 4}
