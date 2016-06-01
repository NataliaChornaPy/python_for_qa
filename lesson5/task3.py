# Write a script to parse habraharb_all.xml and print each article's title, author and all categories.
import xml.etree.ElementTree as etree


def main():
    course_xml = etree.parse('habraharb_all.xml')

    root = course_xml.getroot()
    print root
    for module in root.iter('title'):
        print 'Title----------------',module.text.strip()
    for module in root.iter('author'):
        print 'Author--------',module.text.strip()
    for module in root.iter('category'):
        print  "ARTICLES---------------------------------------", module.text.strip()


if __name__ == '__main__':
    main()