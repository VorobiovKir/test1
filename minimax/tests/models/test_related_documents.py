from django.test import TestCase
from minimax.models import (
    Technology, TechnologyType,
    Solution, SolutionType,
    Document, DocumentType
)


class RelatedDocumentsTestCase(TestCase):
    def setUp(self):
        self.doctype = DocumentType.objects.create(name='Test Document Type')
        self.techtype = TechnologyType.objects.create(name='Test Type')
        self.soltype = SolutionType.objects.create(name='Test Type')
        self.technology = Technology.objects.create(name='Test Technology', type=self.techtype)
        self.solution = Solution.objects.create(name='Test Technology', type=self.soltype)

    # Document Type "ALL"

    def test_technology_relation_all(self):
        doc = Document.objects.create(title='Technologies ALL',
                                      technology_relation_type=Document.RELATION_TYPE_ALL,
                                      type=self.doctype)
        technology = Technology.objects.create(name='Test', type=self.techtype)
        self.assertEqual(technology.all_related_documents.all().count(), 1)
        doc.delete()

    def test_solution_relation_all(self):
        doc = Document.objects.create(title='Solutions ALL',
                                      solution_relation_type=Document.RELATION_TYPE_ALL,
                                      type=self.doctype)
        solution = Solution.objects.create(name='Test', type=self.soltype)
        self.assertEqual(solution.all_related_documents.all().count(), 1)
        doc.delete()

    # Document Type "By item"

    def test_technology_relation_item(self):
        Technology.objects.create(name='Test 3', type=self.techtype)
        Technology.objects.create(name='Test 5', type=self.techtype)
        Technology.objects.create(name='Test 7', type=self.techtype)

        technology = Technology.objects.create(name='Test 2', type=self.techtype)
        doc = Document.objects.create(title='Technologies by item',
                                      technology_relation_type=Document.RELATION_TYPE_BY_ITEM,
                                      type=self.doctype)
        doc.related_technologies.add(technology)
        doc.save()

        self.assertEqual(technology.all_related_documents.all().count(), 1)
        doc.delete()

    def test_solution_relation_item(self):
        Solution.objects.create(name='Test 3', type=self.soltype)
        Solution.objects.create(name='Test 5', type=self.soltype)
        Solution.objects.create(name='Test 7', type=self.soltype)
        solution = Solution.objects.create(name='Test 2', type=self.soltype)
        doc = Document.objects.create(title='Solutions by item',
                                      solution_relation_type=Document.RELATION_TYPE_BY_ITEM,
                                      type=self.doctype)
        doc.related_solutions.add(solution)
        doc.save()

        self.assertEqual(solution.all_related_documents.all().count(), 1)
        doc.delete()

    # Document Type "By type"

    def test_technology_relation_type(self):
        Technology.objects.create(name='Test 1', type=self.techtype)
        Technology.objects.create(name='Test 3', type=self.techtype)
        newtype = TechnologyType.objects.create(name='New Tech Type')
        doc = Document.objects.create(title='Technology by type',
                                      technology_relation_type=Document.RELATION_TYPE_BY_TYPE,
                                      type=self.doctype)
        doc.related_technology_types.add(newtype)
        doc.save()

        docs = []
        for tech in Technology.objects.filter(type=newtype).all():
            docs += tech.all_related_documents.all()
        self.assertEqual(len(docs), 0)

        Technology.objects.create(name='New technology', type=newtype)
        docs = []
        for tech in Technology.objects.filter(type=newtype).all():
            docs += tech.all_related_documents.all()
        self.assertEqual(len(docs), 1)
        doc.delete()

    def test_solution_relation_type(self):
        Solution.objects.create(name='New solution 1', type=self.soltype)
        Solution.objects.create(name='New solution 3', type=self.soltype)
        newtype = SolutionType.objects.create(name='New Solution Type')
        doc = Document.objects.create(title='Solution by type',
                                      solution_relation_type=Document.RELATION_TYPE_BY_TYPE,
                                      type=self.doctype)
        doc.related_solution_types.add(newtype)
        doc.save()

        docs = []
        for sol in Solution.objects.filter(type=newtype).all():
            docs += sol.all_related_documents.all()
        self.assertEqual(len(docs), 0)

        Solution.objects.create(name='New solution', type=newtype)
        docs = []
        for sol in Solution.objects.filter(type=newtype).all():
            docs += sol.all_related_documents.all()
        self.assertEqual(len(docs), 1)
        doc.delete()
