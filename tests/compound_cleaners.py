__author__ = ["Francisco Clavero"]
__description__ = "Test suite for compound cleaners."
__email__ = ["fcoclavero32@gmail.com"]
__status__ = "Prototype"

from datetime import datetime

from unittest import TestCase


# noinspection SpellCheckingInspection
class EnglishTestCase(TestCase):
    """Test that a dirty text is cleaned as expected."""

    text: str = "   thiss is a bery :" "{ñdirti text!  "
    """Dirty text for tests."""

    def test_full_clean(self) -> None:
        """Test the `full_clean` function."""
        from ..compound_cleaners.en import full_clean

        start = datetime.now()
        clean_text = full_clean(self.text)
        self.assertEqual(clean_text, "dirty text !")
        print("Processing complete in %s" % (datetime.now() - start))

    def test_soft_clean(self) -> None:
        """Test the `soft_clean` function."""
        from ..compound_cleaners.en import soft_clean

        start = datetime.now()
        clean_text = soft_clean(self.text)
        self.assertEqual(clean_text, "this is a very dirty text!")
        print("Processing complete in %s" % (datetime.now() - start))


# noinspection SpellCheckingInspection
class SpanishTestCase(TestCase):
    """Test that a dirty text is cleaned as expected."""

    text: str = (
        "   AraucanÃ­a, la manera presora con la cual "
        "estan atacando al pueblo mapuche.el desempleo  "
    )
    """Dirty text for tests."""

    def test_full_clean(self) -> None:
        """Test the `full_clean` function."""
        from ..compound_cleaners.es import full_clean

        start = datetime.now()
        clean_text = full_clean(self.text)
        self.assertEqual(
            clean_text,
            "araucano , manera presora estan atacar poblar mapuche.el desempleo",
        )
        print("Processing complete in %s" % (datetime.now() - start))

    def test_soft_clean(self) -> None:
        """Test the `soft_clean` function."""
        from ..compound_cleaners.es import soft_clean

        start = datetime.now()
        clean_text = soft_clean(self.text)
        self.assertEqual(
            clean_text,
            (
                "araucana, la manera presora con la cual "
                "estan atacando al pueblo mapuche.el desempleo"
            ),
        )
        print("Processing complete in %s" % (datetime.now() - start))
