% NOTE: 
% Test script N1
% Check "*IDN?" and "*RST"
%


%% include 'aDevice'

Fern.load('aDevice')

%%

clc

COM_port = 3;

Box = Hall_box(COM_port);

try
    disp('Test 1: RST')
    Box.RST;
    adev_utils.Wait(1, 'Wait for reboot')
    disp(' ')

    disp('Test 1: IDN')
    resp = Box.IDN;
    disp(['Resp = <' resp '>'])

catch err
    delete(Box);
    warning([newline 'Device is closed in error section'])
    rethrow(err);
end


delete(Box)
disp([newline 'Device is closed'])