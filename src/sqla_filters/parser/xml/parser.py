from xml.etree import ElementTree
from typing import Any

from sqla_filters.nodes.base import TreeNode
from sqla_filters.nodes.logical import(
    OrNode,
    AndNode,
    LOGICAL_NODES
)
from sqla_filters.nodes.operational import OPERATIONAL_NODES
from sqla_filters.tree import SqlaFilterTree
from sqla_filters.parser.base import BaseSqlaParser
from .exceptions import XMLFiltersParserTypeError


def validate_element(e_type, e_value) -> bool:
    pass


class XMLFiltersParser(BaseSqlaParser):
    def __init__(self, data: str, attr_sep: str='.'):
        return super(XMLFiltersParser, self).__init__(data, attr_sep)

    def _create_node(self, key: str, data: Any) -> TreeNode:
        if key == 'and' or key == 'or':
            return LOGICAL_NODES[key]()
        elif key == 'operator':
            attr = data.find('attribute', None)
            operator = data.find('operator', None)
            value = data.find('value', None)
            attr_sep = data.find('separator', None)
            return OPERATIONAL_NODES[operator.text if operator != None else None](
                attr.text if attr != None else '',
                value.text if value != None else None,
                attr_sep=attr_sep.text if attr_sep != None else self._attr_sep
            )
        else:
            raise XMLFiltersParserTypeError('Unknown key.')

    def _generate_nodes(self, xml_element: ElementTree.Element) -> TreeNode:
        node = None
        for child in xml_element:
            r_type: str = child.attrib['type']
            r_data: ElementTree.Element = child.getchildren()[0]
            node = self._create_node(r_type, r_data)
            if isinstance(node, AndNode) or isinstance(node, OrNode):
                node.childs.append(self._generate_nodes(r_data))
        return node

    def _generate_filters_tree(self) -> SqlaFilterTree:
        xml_root = ElementTree.fromstring(self._raw_data)
        print(xml_root)
        return SqlaFilterTree(self._generate_nodes(xml_root))
