from backup.controller.api import (HitterController, PitcherController)


class Router():
    @route(
        function_id='h01',
        path='/api/records/v1/hitter/{personal_id}',
        methon='get')
    def get_hitter_records(self, event, query, personal_id):
        """
        """
        name = query.get('name', None) if query is not None else None
        year = query.get('year', None) if query is not None else None

    @route(
        function_id='h02',
        path='/api/records/v1/hitterTotal/{personal_id}',
        methon='get')
    def get_hitter_total_records(self, event, query, personal_id):
        """
        """
        name = query.get('name', None) if query is not None else None

    @route(
        function_id='h03', path='/api/records/v1/hitters/{year}', methon='get')
    def get_hitters_year_records(self, event, query, year):
        """
        """
        pass

    @route(
        function_id='p01',
        path='/api/records/v1/pitcher/{personal_id}',
        methon='get')
    def get_pitcher_records(self, event, query, personal_id):
        """
        """
        name = query.get('name', None) if query is not None else None
        year = query.get('year', None) if query is not None else None
