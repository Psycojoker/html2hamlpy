from  test_helper import unittest, render

class HtmlToHamlPyTest(unittest.TestCase):
    def test_doctype(self):
        self.assertEqual('!!!', render("<!DOCTYPE html>"))
        self.assertEqual('!!! 1.1', render('<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">'))
        self.assertEqual('!!! Strict', render('<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">'))
        self.assertEqual('!!! Frameset', render('<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Frameset//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-frameset.dtd">'))
        self.assertEqual('!!! Mobile 1.2', render('<!DOCTYPE html PUBLIC "-//WAPFORUM//DTD XHTML Mobile 1.2//EN" "http://www.openmobilealliance.org/tech/DTD/xhtml-mobile12.dtd">'))
        self.assertEqual('!!! Basic 1.1', render('<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML Basic 1.1//EN" "http://www.w3.org/TR/xhtml-basic/xhtml-basic11.dtd">'))
        self.assertEqual('!!!', render('<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">'))
        self.assertEqual('!!! Strict', render('<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">'))
        self.assertEqual('!!! Frameset', render('<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Frameset//EN" "http://www.w3.org/TR/html4/frameset.dtd">'))
        self.assertEqual('!!!', render('<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">'))

    def test_no_tag_name_for_div_if_class_or_id_is_present(self):
        self.assertEqual('#foo', render('<div id="foo"></div>'))
        self.assertEqual('.foo', render('<div class="foo"></div>'))

    def test_multiple_class_names(self):
        self.assertEqual('.foo.bar.baz', render('<div class=" foo bar baz "></div>'))

    def test_class_with_dot_and_hash(self):
        self.assertEqual('%div{class:"foo.bar"}', render("<div class='foo.bar'></div>"))
        self.assertEqual('%div{class:"foo#bar"}', render("<div class='foo#bar'></div>"))
        self.assertEqual('.foo.bar{class:"foo#bar foo.bar"}', render("<div class='foo foo#bar bar foo.bar'></div>"))

    def test_id_with_dot_and_hash(self):
        self.assertEqual('%div{id:"foo.bar"}', render("<div id='foo.bar'></div>"))
        self.assertEqual('%div{id:"foo#bar"}', render("<div id='foo#bar'></div>"))

if __name__ == '__main__':
    unittest.main()
