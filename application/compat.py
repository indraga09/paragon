"""
PySide2/PySide6 compatibility layer.

This module provides a unified interface for both PySide2 and PySide6,
allowing the application to work with either version.
"""

import sys

# Try to import PySide6 first (preferred for Apple Silicon and newer systems)
try:
    from PySide6 import QtCore, QtGui, QtWidgets
    from PySide6.QtCore import *
    from PySide6.QtGui import *
    from PySide6.QtWidgets import *
    
    PYSIDE_VERSION = 6
    print(f"Using PySide6 (Qt {QtCore.qVersion()})")
    
except ImportError:
    try:
        from PySide2 import QtCore, QtGui, QtWidgets
        from PySide2.QtCore import *
        from PySide2.QtGui import *
        from PySide2.QtWidgets import *
        
        PYSIDE_VERSION = 2
        print(f"Using PySide2 (Qt {QtCore.qVersion()})")
        
    except ImportError:
        raise ImportError(
            "Neither PySide6 nor PySide2 could be imported. "
            "Please install one of them: 'pip install PySide6' or 'pip install PySide2'"
        )

# Export commonly used classes and functions for easy importing
__all__ = [
    # Core Qt modules
    'QtCore', 'QtGui', 'QtWidgets',
    
    # Version info
    'PYSIDE_VERSION',
    
    # Common QtCore classes
    'QObject', 'QThread', 'QTimer', 'QModelIndex', 'QAbstractListModel',
    'QAbstractItemModel', 'QSortFilterProxyModel', 'Signal', 'Slot',
    
    # Common QtGui classes
    'QPixmap', 'QIcon', 'QFont', 'QFontMetrics', 'QColor', 'QStandardItemModel',
    'QStandardItem', 'QFontDatabase',
    
    # Common QtWidgets classes
    'QApplication', 'QWidget', 'QMainWindow', 'QDialog', 'QVBoxLayout',
    'QHBoxLayout', 'QGridLayout', 'QLabel', 'QPushButton', 'QLineEdit',
    'QTextEdit', 'QComboBox', 'QListView', 'QTreeView', 'QTableView',
    'QProgressDialog', 'QFileDialog', 'QMessageBox', 'QStyleFactory',
    'QGraphicsTextItem'
]

def get_pyside_version():
    """Return the PySide version being used (2 or 6)."""
    return PYSIDE_VERSION

def is_pyside6():
    """Return True if using PySide6, False if using PySide2."""
    return PYSIDE_VERSION == 6

def is_pyside2():
    """Return True if using PySide2, False if using PySide6."""
    return PYSIDE_VERSION == 2