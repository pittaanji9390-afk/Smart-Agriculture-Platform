# Contributing to AgriSphere OS 🌱

Thank you for your interest in contributing to **AgriSphere OS**! We welcome contributions from agronomists, software engineers, data scientists, and open-source enthusiasts.

---

## 📜 Code of Conduct
We are committed to providing a welcoming, inclusive, and harassment-free experience for everyone. Please be respectful and constructive in all communications.

---

## 🛠️ Development Setup

### 1. Fork & Clone Repository
```bash
git clone https://github.com/pittaanji9390-afk/Smart-Agriculture-Platform.git
cd Smart-Agriculture-Platform
```

### 2. Create Virtual Environment
```bash
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On Linux/macOS:
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements-dev.txt
```

---

## 🧪 Testing & Code Quality Guidelines

Before submitting a Pull Request, make sure all automated checks pass locally:

### Run Full Test Suite with Coverage:
```bash
pytest tests/ -v --cov=. --cov-report=term-missing
```

### Run Linters & Type Checking:
```bash
ruff check .
flake8 .
black --check .
mypy backend services edge_gateway
```

### Run Dependency Vulnerability Audit:
```bash
pip-audit -r requirements.txt
```

---

## 🌿 Branching Strategy & Git Commit Convention

We follow standard Conventional Commits:
- `feat:` New features or agronomic models
- `fix:` Bug fixes or calculation corrections
- `docs:` Documentation updates
- `test:` Adding or updating unit/integration tests
- `refactor:` Code refactoring without behavioral change
- `chore:` Dependency or build system updates

### Example:
```bash
git checkout -b feat/satellite-vari-index
git commit -m "feat(gis): add Visible Atmospherically Resistant Index (VARI) calculation"
git push origin feat/satellite-vari-index
```

---

## 📬 Submitting a Pull Request
1. Ensure your branch is rebased on the latest `main` branch.
2. Fill out the Pull Request template with details about what your change accomplishes.
3. Link any relevant issue numbers (e.g., `Closes #12`).
4. Ensure all CI pipeline checks pass.
