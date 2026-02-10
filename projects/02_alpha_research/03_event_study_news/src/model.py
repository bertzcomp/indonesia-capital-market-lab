from sklearn.ensemble import RandomForestClassifier
from sklearn.calibration import CalibratedClassifierCV
from sklearn.preprocessing import StandardScaler

def train_model(X, y):
    scaler = StandardScaler()
    Xs = scaler.fit_transform(X)

    rf = RandomForestClassifier(
        n_estimators=300,
        max_depth=5,
        class_weight="balanced",
        random_state=42
    )

    model = CalibratedClassifierCV(rf, method="isotonic", cv=3)
    model.fit(Xs, y)

    return model, scaler
