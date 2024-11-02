# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import pet_adoption_pb2 as pet__adoption__pb2

GRPC_GENERATED_VERSION = '1.67.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in pet_adoption_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class PetAdoptionStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetPets = channel.unary_unary(
                '/petAdoption.PetAdoption/GetPets',
                request_serializer=pet__adoption__pb2.Empty.SerializeToString,
                response_deserializer=pet__adoption__pb2.PetsResponse.FromString,
                _registered_method=True)
        self.AdoptPet = channel.unary_unary(
                '/petAdoption.PetAdoption/AdoptPet',
                request_serializer=pet__adoption__pb2.PetIdRequest.SerializeToString,
                response_deserializer=pet__adoption__pb2.AdoptionResponse.FromString,
                _registered_method=True)
        self.RegisterPet = channel.unary_unary(
                '/petAdoption.PetAdoption/RegisterPet',
                request_serializer=pet__adoption__pb2.Pet.SerializeToString,
                response_deserializer=pet__adoption__pb2.AdoptionResponse.FromString,
                _registered_method=True)
        self.SearchPets = channel.unary_unary(
                '/petAdoption.PetAdoption/SearchPets',
                request_serializer=pet__adoption__pb2.PetSearchRequest.SerializeToString,
                response_deserializer=pet__adoption__pb2.PetsResponse.FromString,
                _registered_method=True)


class PetAdoptionServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetPets(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AdoptPet(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RegisterPet(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SearchPets(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PetAdoptionServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetPets': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPets,
                    request_deserializer=pet__adoption__pb2.Empty.FromString,
                    response_serializer=pet__adoption__pb2.PetsResponse.SerializeToString,
            ),
            'AdoptPet': grpc.unary_unary_rpc_method_handler(
                    servicer.AdoptPet,
                    request_deserializer=pet__adoption__pb2.PetIdRequest.FromString,
                    response_serializer=pet__adoption__pb2.AdoptionResponse.SerializeToString,
            ),
            'RegisterPet': grpc.unary_unary_rpc_method_handler(
                    servicer.RegisterPet,
                    request_deserializer=pet__adoption__pb2.Pet.FromString,
                    response_serializer=pet__adoption__pb2.AdoptionResponse.SerializeToString,
            ),
            'SearchPets': grpc.unary_unary_rpc_method_handler(
                    servicer.SearchPets,
                    request_deserializer=pet__adoption__pb2.PetSearchRequest.FromString,
                    response_serializer=pet__adoption__pb2.PetsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'petAdoption.PetAdoption', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('petAdoption.PetAdoption', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class PetAdoption(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetPets(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/petAdoption.PetAdoption/GetPets',
            pet__adoption__pb2.Empty.SerializeToString,
            pet__adoption__pb2.PetsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def AdoptPet(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/petAdoption.PetAdoption/AdoptPet',
            pet__adoption__pb2.PetIdRequest.SerializeToString,
            pet__adoption__pb2.AdoptionResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def RegisterPet(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/petAdoption.PetAdoption/RegisterPet',
            pet__adoption__pb2.Pet.SerializeToString,
            pet__adoption__pb2.AdoptionResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def SearchPets(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/petAdoption.PetAdoption/SearchPets',
            pet__adoption__pb2.PetSearchRequest.SerializeToString,
            pet__adoption__pb2.PetsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
