import os
from typing import Dict

from sqla_filters.parser.xml import XMLFiltersParser
from sqla_filters.nodes.logical import AndNode
from sqla_filters.nodes.operational import (
    EqNode,
    NotEqNode,
    NullNode,
    NotNullNode,
    GtNode,
    GteNode,
    LtNode,
    LteNode,
    InNode,
    NotInNode,
    ContainsNode,
    LikeNode
)


class TestParserBase(object):
    _resources: Dict = {}

    def _get_parser(self, key: str) -> XMLFiltersParser:
        file_path = os.path.join(
            os.path.dirname(__file__),
            self._resources[key]
        )
        xml_data = open(file_path).read()
        return XMLFiltersParser(xml_data)


class TestXMLEquality(TestParserBase):
    def setup_class(self):
        self._resources['eq'] = 'resources/eq/eq.xml'
        self._resources['eq_rel'] = 'resources/eq/eq_rel.xml'

    def test_01_eq(self):
        parser = self._get_parser('eq')
        assert isinstance(parser.tree.root, AndNode)
        assert len(parser.tree.root.childs) == 1
        assert isinstance(parser.tree.root.childs[0], EqNode)